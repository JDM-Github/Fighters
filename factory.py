from kivy.factory import Factory
from fighter import Shooter
Factory.register("ScreenManager", module="kivy.uix.screenmanager")
Factory.register("Screen", module="kivy.uix.screenmanager")

Factory.register("PeaShooter", cls=Shooter)
