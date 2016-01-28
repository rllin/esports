import gmail
import os.path

# InvokerPracticeResearch:invoker1
def download_attachments(username, password, label, extension,  save_dir):
    ''' username: username of the gmail account (make sure you enable login for less secure apps)
        password: password of the gmail account
        label: label of the messages with attachments
        extension: file extension expected (e.g. .json)
        save_dir: path of directory you want attachments saved in
    '''
    g = gmail.login(username, password)
    mail = g.mailbox(label).mail()
    for m in mail:
        m.fetch()
        for attach in m.attachments:
            if os.path.splitext(attach.name)[1] == extension:
                attach.save(save_dir)
                print 'saving ' + attach.name + ' from ' + m.fr
    g.logout() 
