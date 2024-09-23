class DataMixin:
    paginate_by = 3

class SpecMixin:
    login_url = '/admin/'
    template_name = 'wowsite/forms/add.html'
    
    def get_success_url(self):
        return self.object.get_absolute_url()