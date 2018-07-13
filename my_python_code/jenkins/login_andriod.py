from jenkinsapi.jenkins import Jenkins
import jenkinsapi

def getSCMInfroFromLatestGoodBuild(url, jobName, username=None, password=None):
    J = Jenkins(url, username, password)
    job = J[jobName]
    lgb = job.get_last_good_build()
    print(jenkinsapi.__version__)
    return lgb.get_revision()

if __name__ == '__main__':
    print (getSCMInfroFromLatestGoodBuild('http://localhost:8080', 'test_coach_pad_app','luhuiyu','123456'))