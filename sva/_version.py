try:
    import dunamai as _dunamai

    __version__ = _dunamai.Version.from_any_vcs().serialize()
    del _dunamai
except ImportError:
    __version__ = "dev"
