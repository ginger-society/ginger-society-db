from ginger.db import models



db_types = (
    
        ("rdbms", "rdbms"),
    
        ("cache", "cache"),
    
        ("documentdb", "documentdb"),
    
)




build_status_options = (
    
        ("running", "running"),
    
        ("failed", "failed"),
    
        ("passing", "passing"),
    
        ("dormant", "dormant"),
    
)




package_types = (
    
        ("library", "library"),
    
        ("executable", "executable"),
    
)




service_types = (
    
        ("portal", "Portal"),
    
        ("rpcendpoint", "RPCEndpoint"),
    
)




envs = (
    
        ("dev", "dev"),
    
        ("stage", "stage"),
    
        ("prod", "prod"),
    
)




class dbschema(models.Model):
        """DB Schema"""
    
    
     
        name = models.CharField(  max_length=100,         )
    
     
        description = models.CharField(  max_length=500,     blank=True,null=True,     )
    
     
        created_at = models.DateTimeField(         auto_now_add=True,  )
    
     
        updated_at = models.DateTimeField(        auto_now=True,   )
    
     
        data = models.TextField(  max_length=10000,     null=True,     )
    
     
        group_id = models.CharField(  max_length=500,     blank=True,null=True,     )
    
     
        identifier = models.CharField(  max_length=100,     blank=True,null=True,     )
    
     
        organization_id = models.CharField(  max_length=100,     blank=True,null=True,     )
    
     
        repo_origin = models.CharField(  max_length=200,     blank=True,null=True,     )
    
     
        db_type = models.CharField( choices=db_types, max_length=50,   default='rdbms',      )
    
        class Meta:
            db_table = "dbschema"




class dbschema_branch(models.Model):
        """"""
    
    
     
        parent = models.ForeignKey('dbschema',related_name = 'definitions', on_delete=models.CASCADE,          )
    
     
        branch_name = models.CharField(  max_length=100,         )
    
     
        data = models.TextField(  max_length=10000,     null=True,     )
    
     
        created_at = models.DateTimeField(         auto_now_add=True,  )
    
     
        updated_at = models.DateTimeField(        auto_now=True,   )
    
     
        version = models.CharField(  max_length=50,     blank=True,null=True,     )
    
     
        pipeline_status = models.CharField( choices=build_status_options, max_length=70,     blank=True,null=True,     )
    
        class Meta:
            db_table = "dbschema_branch"




class templates(models.Model):
        """All templates are public"""
    
    
     
        short_name = models.CharField(  max_length=100,         )
    
     
        description = models.TextField(  max_length=600,         )
    
     
        repo_link = models.CharField(  max_length=100,         )
    
     
        identifier = models.CharField(  max_length=40,         )
    
        class Meta:
            db_table = "templates"




class service(models.Model):
        """"""
    
    
     
        identifier = models.CharField(  max_length=50,         )
    
     
        group_id = models.CharField(  max_length=100,         )
    
     
        db_schema_id = models.CharField(  max_length=100,     blank=True,null=True,     )
    
     
        tables_json = models.CharField(  max_length=1000,     blank=True,null=True,     )
    
     
        dependencies_json = models.CharField(  max_length=1000,     blank=True,null=True,     )
    
     
        service_type = models.CharField( choices=service_types, max_length=50,   default='RPCEndpoint',      )
    
     
        lang = models.CharField(  max_length=50,     blank=True,null=True,     )
    
     
        description = models.TextField(  max_length=2000,     null=True,     )
    
     
        organization_id = models.CharField(  max_length=100,     blank=True,null=True,     )
    
     
        repo_origin = models.CharField(  max_length=200,     blank=True,null=True,     )
    
     
        cache_schema_id = models.CharField(  max_length=250,     blank=True,null=True,     )
    
        class Meta:
            db_table = "service"




class service_envs(models.Model):
        """"""
    
    
     
        parent = models.ForeignKey('service',related_name = 'envs', on_delete=models.CASCADE,          )
    
     
        spec = models.TextField(  max_length=35000,         )
    
     
        env = models.CharField( choices=envs, max_length=10,         )
    
     
        base_url = models.CharField(  max_length=100,         )
    
     
        updated_at = models.DateTimeField(      null=True,   auto_now=True,   )
    
     
        version = models.CharField(  max_length=30,   default='0.0.0',      )
    
     
        pipeline_status = models.CharField( choices=build_status_options, max_length=70,     blank=True,null=True,     )
    
        class Meta:
            db_table = "service_envs"




class package(models.Model):
        """packages such as libraries , executables"""
    
    
     
        identifier = models.CharField(  max_length=100,         )
    
     
        package_type = models.CharField( choices=package_types, max_length=50,         )
    
     
        lang = models.CharField(  max_length=50,         )
    
     
        group_id = models.CharField(  max_length=100,     blank=True,null=True,     )
    
     
        updated_at = models.DateTimeField(        auto_now=True,   )
    
     
        created_at = models.DateTimeField(      null=True,    auto_now_add=True,  )
    
     
        organization_id = models.CharField(  max_length=100,     blank=True,null=True,     )
    
     
        description = models.CharField(  max_length=25000,     blank=True,null=True,     )
    
     
        dependencies_json = models.CharField(  max_length=1000,     blank=True,null=True,     )
    
     
        repo_origin = models.CharField(  max_length=200,     blank=True,null=True,     )
    
        class Meta:
            db_table = "package"




class package_env(models.Model):
        """"""
    
    
     
        version = models.CharField(  max_length=50,         )
    
     
        env = models.CharField( choices=envs, max_length=10,         )
    
     
        parent = models.ForeignKey('package',related_name = 'envs', on_delete=models.CASCADE,          )
    
     
        pipeline_status = models.CharField( choices=build_status_options, max_length=70,     blank=True,null=True,     )
    
        class Meta:
            db_table = "package_env"




class organization(models.Model):
        """"""
    
    
     
        slug = models.CharField(  max_length=100,         )
    
     
        group_id = models.CharField(  max_length=100,         )
    
     
        is_active = models.BooleanField(default=True,          )
    
     
        blocks_positions = models.TextField(  max_length=40000,     null=True,     )
    
     
        name = models.CharField(  max_length=100,     blank=True,null=True,     )
    
        class Meta:
            db_table = "organization"



