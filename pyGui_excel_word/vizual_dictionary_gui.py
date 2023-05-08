# https://pypi.org/project/traitsui/
# 1º (base) D:\phytonSpace\miBasic\A_pyVSCode\pyGui_excel_word>conda install traits
# 2º (base) D:\phytonSpace\miBasic\A_pyVSCode\pyGui_excel_word>conda install traitsui
#  
from traits.api import HasTraits, Str, Range, Enum
from traitsui.api import Item, RangeEditor, View

class Person(HasTraits):
    name = Str('Jane Doe')
    age = Range(low=0)
    gender = Enum('female', 'male')

person = Person(age=30)

person_view = View(
    Item('name'),
    Item('gender'),
    Item('age', editor=RangeEditor(mode='spinner', low=0, high=150)),
    buttons=['OK', 'Cancel'],
    resizable=True,
)

person.configure_traits(view=person_view)