import json
from todoist_api_python.api import TodoistAPI
from config import *
from flask import escape

#get open To Do list tasks from Todoist 
def get_todo_content():
    
    todoist = TodoistAPI(USERTOKEN)
    project_dict = {}
    open_tasks = []
    
    try:
        projects = todoist.get_projects()
        #get all active projects for labeling and color coding
        for project in projects:
            project_dict[project.id] = project
    except Exception as error:
        return(error)

    try:
        tasks = todoist.get_tasks()
        #get all open tasks from todoist api
        for task in tasks:
            open_tasks.append(task)
         
    except Exception as error:
        return(error)

    #load in tasks and projects to be formatted, return when done
    return(make_todo_items(project_dict, open_tasks))


#returns  alist of html input blocks with current oepn tasks, color coded by project
def make_todo_items(projects, tasks):
    items = []
    task_num = 1
    for open_task in tasks:
        task_id = open_task.id
        task_num_str = str(task_num)
        task_project = projects[str(escape(open_task.project_id))]
        
        task_html = "<div class='alert' style='padding:5px;background-color:"+TODOIST_COLORS[str(escape(task_project.color))]+"'><input type='checkbox' id='task"+task_num_str+"' name='task"+task_num_str+"' value='"+task_id+"'>"
        task_html+= "<label for='task"+task_num_str+"'>&nbsp;&nbsp;<b>"+str(escape(task_project.name))+"//</b> "+str(escape(open_task.content))+"</label></div>"
        items.append(task_html)
        task_num+=1
    return items
