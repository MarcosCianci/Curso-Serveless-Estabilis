import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime

dao = BaseDAO('table5')

for i in range(10):
    dao.put_item({'uers':str(i)})
