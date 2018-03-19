#!/usr/bin/python

import os

from ansible.errors import AnsibleError
from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, task_vars=None):
        '''
        Run an Ansible action from a local script.

        :param task_vars:
        :return:
        '''

        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(task_vars)
        source = self._task.args.get('src')

        if source is None:
            raise AnsibleError("You must define a source.")

        if self._task._role is not None:
            source = self._loader.path_dwim_relative(self._task._role._role_path, 'python_scripts', source)
        else:
            source = self._loader.path_dwim_relative(self._loader.get_basedir(), 'python_scripts', source)

        source = os.path.abspath(source)

        temp_vars = task_vars.copy()
        temp_vars['meta_action'] = self
        temp_vars['meta_source'] = source

        old_cwd = os.getcwd()
        os.chdir(os.path.dirname(source))
        execfile(source, temp_vars)  # Don't worry. It's going to be awesome.
        os.chdir(old_cwd)

        replace_vars = self._task.args.get('vars', list())

        facts = dict()
        for replace_var in replace_vars:
            facts[replace_var] = temp_vars.get(replace_var)

        result['ansible_facts'] = facts

        return result
