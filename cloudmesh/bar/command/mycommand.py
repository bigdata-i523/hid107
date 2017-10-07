from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.bar.api.manager import Manager
import os
import urllib.request,re

class BarCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def  video_time_sum():
        def pageload(url):
            web_page=urllib.request.urlopen(url)
            content=web_page.read().decode(errors="replace")
            web_page.close()

            return content

        course_page=pageload("https://github.com/cloudmesh/classes/tree/master/docs/source/i523/2017/course")

        rst_lst=re.findall('(?<=<a href="/cloudmesh/classes/blob/master/docs/source/i523/2017/course/).+?(?=.rst)',course_page)

        for section_name in rst_lst:
            total_time_lst=[]
            section_time=0

            k="https://github.com/cloudmesh/classes/blob/master/docs/source/i523/2017/course/"+section_name+".rst"
            print(k)
            section_page=pageload(k)
            time_lst=re.findall('(?<=Video:).+?(?=: )',section_page)
            print(time_lst)

            for time in time_lst:
                if section_name != "sport":
                   total_time=0
                   time_format=time.split(":")
                   minute=re.findall(r"\d+\.?\d*",time_format[0])
                   sec=re.findall(r"\d+\.?\d*",time_format[1])
                   total_time=int(minute[0])+float(int(sec[0])/60)
                   total_time_lst.append(total_time)
                else:
                   total_time=0
                   time_format=time.split("min")
                   minute=re.findall(r"\d+\.?\d*",time_format[0])
                   sec=re.findall(r"\d+\.?\d*",time_format[1])
                   total_time=int(minute[0])+float(int(sec[0])/60)
                   total_time_lst.append(total_time)


            for t_time in total_time_lst:
                section_time+=float(t_time)

            print("The total video time of section: ",section_name,"is ", section_time,"min")

        
       
