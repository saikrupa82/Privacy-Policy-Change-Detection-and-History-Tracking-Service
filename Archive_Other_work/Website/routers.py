class AuthRouter:
    """
    A router to control all database operations on models in the
    authen application.
    """
    route_app_labels = {'authen'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read authen models go to default.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write authen models go to default.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the authen app.
        """
        if obj1._meta.app_label in self.route_app_labels and obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the authen app only appears in the 'default'
        database.
        """
        if app_label in self.route_app_labels:
            return db == 'default'
        return None


class TrackerRouter:
    """
    A router to control all database operations on models in the
    tracker application.
    """
    route_app_labels = {'tracker'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read tracker models go to 'policy'.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'policy'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write tracker models go to 'policy'.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'policy'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the tracker app.
        """
        if obj1._meta.app_label in self.route_app_labels and obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the tracker app only appears in the 'policy'
        database.
        """
        if app_label in self.route_app_labels:
            return db == 'policy'
        return None
