import warnings
from sklearn.exceptions import InconsistentVersionWarning

# Ignore sklearn version mismatch warning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# Ignore feature-name warnings
warnings.filterwarnings("ignore", category=UserWarning)
