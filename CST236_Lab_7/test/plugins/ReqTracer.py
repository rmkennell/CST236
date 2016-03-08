from nose2.events import Plugin


class ReqTracer(Plugin):
    configSection = "req-tracer"

    def afterSummaryReport(self, event):
        outputFile = open("output.txt", "w")
        for key, item in sorted(Requirements.items()):
            outputFile.write(' ')
            outputFile.write(key)
            for func in item.func_name:
                outputFile.write(' ' + func + ' ')
                outputFile.write('\n')





class JSTrace:
    job_story = ""

    def __init__(self, text):
        self.job_story = text
        self.func_name = []


class RequirementTrace(object):
    req_text = ""

    def __init__(self, text):
        self.req_text = text
        self.func_name = []


Requirements = {}

Stories = []


def story(js):
    def wrapper(func):
        def add_job_and_call(*args, **kwargs):
            for jstory in Stories:
                if jstory.job_story.lower() == js.lower():
                    jstory.func_name.append(func.__name__)
                    break
                else:
                    raise Exception('Stories {0} not defined'.format(js))

            return func(*args, **kwargs)

        return add_job_and_call

    return wrapper


class JobStory(object):
    req_text = ""

    def __init__(self, text):
        self.req_text = text
        self.func_name = []


def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


with open('requirementTest.txt') as f:
    for line in f.readlines():
        if '#00' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)
    for line in f.readline():
        if '*' in line:
            jstory = line.split('', 1)[1]
            Stories.append(JSTrace(jstory.strip()))
