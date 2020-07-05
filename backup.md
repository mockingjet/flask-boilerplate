```python
import sys
import os.path
# add path env
sys.path.append(os.path.realpath('.'))
# remember to import all models
from jetblog import app
from jetblog.database import Model
target_metadata = Model.metadata
```

