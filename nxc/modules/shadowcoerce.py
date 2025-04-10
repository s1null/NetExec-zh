class NXCModule:
    name = "shadowcoerce"
    description = "[已移除] 检查目标是否易受ShadowCoerce漏洞攻击的模块，感谢@Shutdown和@topotam"
    supported_protocols = ["smb"]
    opsec_safe = True
    multiple_hosts = True

    def options(self, context, module_options):
        """
        IPSC             Use IsPathShadowCopied (default: False). ex. IPSC=true
        LISTENER         Listener IP address (default: 127.0.0.1)
        """
        self.ipsc = False
        self.listener = "127.0.0.1"
        if "LISTENER" in module_options:
            self.listener = module_options["LISTENER"]
        if "IPSC" in module_options:
            # Any string that's not empty can be casted to bool True
            self.ipsc = bool(module_options["IPSC"])

    def on_login(self, context, connection):
        context.log.fail('[REMOVED] This module moved to the new module "coerce_plus"')