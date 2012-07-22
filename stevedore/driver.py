from .hook import HookManager


class DriverManager(HookManager):
    """Load a single plugin with a given name from the namespace.

    :param namespace: The namespace for the entry points.
    :type namespace: str
    :param name: The name of the driver to load.
    :type name: str
    :param invoke_on_load: Boolean controlling whether to invoke the
        object returned by the entry point after the driver is loaded.
    :type invoke_on_load: bool
    :param invoke_args: Positional arguments to pass when invoking
        the object returned by the entry point. Only used if invoke_on_load
        is True.
    :type invoke_args: tuple
    :param invoke_kwds: Named arguments to pass when invoking
        the object returned by the entry point. Only used if invoke_on_load
        is True.
    :type invoke_kwds: dict
    """

    def __init__(self, namespace, name,
                 invoke_on_load=False, invoke_args=(), invoke_kwds={}):
        super(HookManager, self).__init__(
            namespace,
            [name],
            invoke_on_load=invoke_on_load,
            invoke_args=invoke_args,
            invoke_kwds=invoke_kwds,
            )
        if not self.extensions:
            raise RuntimeError('No %r driver found' % namespace)
        if len(self.extensions) > 1:
            raise RuntimeError('Multiple %r drivers found: %s' %
                               (namespace,
                                ','.join('%s:%s' % (e.module_name, e.attrs[0])
                                         for e in self.extensions))
                               )