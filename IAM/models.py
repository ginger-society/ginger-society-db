from ginger.db import models



class user(models.Model):
        """User's table"""
    
    
     
        first_name = models.CharField(  max_length=40,     blank=True,null=True,     )
    
     
        last_name = models.CharField(  max_length=40,     blank=True,null=True,     )
    
     
        middle_name = models.CharField(  max_length=40,     blank=True,null=True,     )
    
     
        email_id = models.CharField(  max_length=100,         )
    
     
        mobile_number = models.CharField(  max_length=15,     blank=True,null=True,     )
    
     
        created_at = models.DateTimeField(         auto_now_add=True,  )
    
     
        updated_at = models.DateTimeField(        auto_now=True,   )
    
     
        password_hash = models.CharField(  max_length=400,     blank=True,null=True,     )
    
     
        is_root = models.BooleanField(default=False,          )
    
        class Meta:
            db_table = "user"




class token(models.Model):
        """tokens like password hashes , TOTP , session tokens etc"""
    
    
     
        session_hash = models.CharField(  max_length=400,     blank=True,null=True,     )
    
     
        user = models.ForeignKey('user',related_name = 'tokens', on_delete=models.CASCADE,          )
    
     
        app = models.ForeignKey('app',on_delete=models.CASCADE,      blank=True,null=True,     )
    
        class Meta:
            db_table = "token"




class app(models.Model):
        """Application"""
    
    
     
        client_id = models.CharField(  max_length=150,         )
    
     
        name = models.CharField(  max_length=50,         )
    
     
        logo_url = models.CharField(  max_length=200,     blank=True,null=True,     )
    
     
        disabled = models.BooleanField(default=False,          )
    
     
        app_url_dev = models.CharField(  max_length=100,     blank=True,null=True,     )
    
     
        app_url_stage = models.CharField(  max_length=100,     blank=True,null=True,     )
    
     
        app_url_prod = models.CharField(  max_length=100,     blank=True,null=True,     )
    
     
        group = models.ForeignKey('group',related_name = 'apps', on_delete=models.SET_NULL,      blank=True,null=True,     )
    
     
        tnc_link = models.CharField(  max_length=500,     blank=True,null=True,     )
    
        class Meta:
            db_table = "app"




class group(models.Model):
        """Groups"""
    
    
     
        identifier = models.CharField(  max_length=50,         )
    
     
        users = models.ManyToManyField('user',related_name = 'groups',           )
    
     
        owners = models.ManyToManyField('user',related_name = 'managed_groups',           )
    
     
        disabled = models.BooleanField(default=False,          )
    
     
        short_text = models.CharField(  max_length=100,     blank=True,null=True,     )
    
        class Meta:
            db_table = "group"




class api_token(models.Model):
        """"""
    
    
     
        parent = models.ForeignKey('group',related_name = 'api_tokens', on_delete=models.CASCADE,          )
    
     
        expiry_date = models.DateField(          )
    
     
        created_at = models.DateTimeField(         auto_now_add=True,  )
    
     
        updated_at = models.DateTimeField(        auto_now=True,   )
    
     
        is_active = models.BooleanField(default=True,          )
    
     
        name = models.CharField(  max_length=100,         )
    
     
        token_str = models.CharField(  max_length=400,     blank=True,null=True,     )
    
        class Meta:
            db_table = "api_token"



