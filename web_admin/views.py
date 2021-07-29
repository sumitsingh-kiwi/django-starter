""" views file"""

import shutil
import os
import datetime
from io import BytesIO
import zipfile

from django.contrib import messages
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from web_admin.constants import PROJECT_DIR
from web_admin.forms import DownloadProjectForm


class DownloadProjectView(View):
    """
    1. used to return the download project form
    2. download the project
    """
    form = DownloadProjectForm

    def get(self, request):
        """ used to return the download project template"""
        return render(request, template_name='download-form.html', context={})

    def post(self, request):
        """ used to download the project """
        data = request.POST
        form = DownloadProjectForm(data)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return redirect(reverse('download-project'))
        project_name, time_stamp = request.POST['project_name'], datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        notification = 'true' if request.POST.get('notification', False) else 'false'

        project_dir = PROJECT_DIR[request.POST['auth_type'] + "-" + notification]

        # call the shell script
        os.system('./create_project.sh {} {} {}'.format(project_dir, project_name, time_stamp))

        path_to_file = '/tmp/{}{}.zip'.format(project_name, time_stamp)
        zip_file = open(path_to_file, 'rb')
        return FileResponse(zip_file)
