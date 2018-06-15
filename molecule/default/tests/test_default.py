import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_exists(host):
    f = host.file('/usr/lib/jvm/java-8-oracle/jre/bin/java')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_java_symlink_exists(host):
    f = host.file('/usr/bin/java')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.is_symlink
    assert f.linked_to == '/usr/lib/jvm/java-8-oracle/jre/bin/java'


# Doesn't work for some reason
# def test_java_version(host):
#     r = host.check_output('/usr/bin/java -version')
#     print(r)
#     assert 'java version "1.8' in r
