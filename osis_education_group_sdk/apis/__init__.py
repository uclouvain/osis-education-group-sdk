
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.groups_api import GroupsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from osis_education_group_sdk.api.groups_api import GroupsApi
from osis_education_group_sdk.api.habilitation_list_api import HabilitationListApi
from osis_education_group_sdk.api.mini_trainings_api import MiniTrainingsApi
from osis_education_group_sdk.api.trainings_api import TrainingsApi
