import shutil
import zipfile

import os
from django.conf import settings
from .utils import get_current_members_with_completed_profile


def zipdir(path, zipf):
    for root, dirs, files in os.walk(path):
        for f in files:
            zipf.write(os.path.join(root, f))


def make_zip(dir, name):
    zip_file_name = os.path.join(settings.MEDIA_ROOT, name)
    try:
        os.remove(zip_file_name)
    except OSError:
        pass
    zip_f = zipfile.ZipFile(zip_file_name, 'w')
    os.chdir(dir)
    zipdir('.', zip_f)
    zip_f.close()


def aggregate_resumes(type, members_with_resumes, resumes_dir):
    if os.path.exists(resumes_dir):
        shutil.rmtree(resumes_dir)
    os.makedirs(resumes_dir)

    for member in members_with_resumes:
        if type == 'year':
            curr_attr = member.graduation_date.year
            attr_dir = os.path.join(resumes_dir, 'Graduating_' + str(curr_attr))
        else:
            curr_attr = member.get_major_display()
            attr_dir = os.path.join(resumes_dir, str(curr_attr))

        if not os.path.exists(attr_dir):
            os.makedirs(attr_dir)
        resume_name = member.last_name + '_' + member.first_name + '_' + member.uniqname + '.pdf'
        shutil.copy(settings.MEDIA_ROOT + '/' + '/'.join(member.resume.url.split('/')[2:]),
                    os.path.join(attr_dir, resume_name))


def zip_resumes():
    resumes_year_dir = os.path.join(settings.MEDIA_ROOT, 'resume_year')
    resumes_major_dir = os.path.join(settings.MEDIA_ROOT, 'resume_major')

    members_with_resumes = get_current_members_with_completed_profile()
    members_with_resumes = members_with_resumes.filter(resume__isnull=False)
    members_with_resumes = members_with_resumes.exclude(resume__exact="")

    aggregate_resumes('year', members_with_resumes, resumes_year_dir)
    aggregate_resumes('major', members_with_resumes, resumes_major_dir)

    make_zip(resumes_year_dir, 'HKN_resumes_by_year.zip')
    make_zip(resumes_major_dir, 'HKN_resumes_by_major.zip')

    print("Updated Resumes Zips")
