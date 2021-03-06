from fabric.api import env, run, cd, prefix, sudo, hosts

from fabric.colors import green, yellow

WEB_ROOT = "/root/"
env.user = "root"
env.key_filename = ["~/.ssh/config"]


@hosts(['SOME_IP'])
def deploy():

    print(yellow("Deploy DO"))

    print(green("Starting deploy"))
    with cd('/root/crawler'):
        run('git pull')
        with prefix('source /root/env/crawler/bin/activate'):
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('deactivate')
        # run('supervisorctl restart all')
        sudo('service nginx restart')

        print(green("Success"))