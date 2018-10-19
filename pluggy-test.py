import pluggy

hookspec = pluggy.HookspecMarker('ttt')
hookimpl = pluggy.HookimplMarker('ttt')


class MySpec:
    @hookspec
    def first_hook(self, arg1, arg2, arg3):
        pass
    @hookspec
    def second_hook(self, arg1, arg2, arg3):
        pass

    @hookspec
    def third_hook(self, arg1, arg2, arg3):
        pass


class Plugin1:
    # may be module with hook functions
    @hookimpl
    def first_hook(self, arg1, arg2, arg3):
        print(self.__class__, arg1, arg2, arg3)
        return '1: ' + str(arg1 + arg2 + arg3)

    @hookimpl
    def second_hook(self, arg1, arg2, arg3):
        print(self.__class__, arg1, arg2, arg3)
        return '2: ' + str(arg1 + arg2 + arg3)

    @hookimpl
    def third_hook(self, arg1, arg2, arg3):
        print(self.__class__, arg1, arg2, arg3)
        return '3: ' + str(arg1 + arg2 + arg3)


class Plugin2:
    # may be module with hook functions
    @hookimpl
    def first_hook(self, arg1, arg2, arg3):
        print(self.__class__, arg1, arg2, arg3)
        return '10: ' + str(arg1 + arg2 + arg3)

    @hookimpl
    def second_hook(self, arg1, arg2, arg3):
        print(self.__class__, arg1, arg2, arg3)
        return '20: ' + str(arg1 + arg2 + arg3)

    @hookimpl
    def third_hook(self, arg1, arg2, arg3):
        print(self.__class__, arg1, arg2, arg3)
        return '30: ' + str(arg1 + arg2 + arg3)


pm = pluggy.PluginManager('ttt')  # project name must equal to in HookspecMarker and HookimplMarker
pm.add_hookspecs(MySpec)
pm.register(Plugin1())  # pass object not class to handle self argument
pm.register(Plugin2())  # pass object not class to handle self argument
hook1_result = pm.hook.first_hook(arg1=1, arg2=2, arg3=3)  # all argument must be named not positional
print(hook1_result)
hook2_result = pm.hook.second_hook(arg1=10, arg2=20, arg3=30)  # all argument must be named not positional
print(hook2_result)
hook3_result = pm.hook.third_hook(arg1=100, arg2=200, arg3=300)  #all argument must be named not positional
print(hook3_result)