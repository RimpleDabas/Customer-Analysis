{
    "metadata": {
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3",
            "language": "python"
        },
        "language_info": {
            "name": "python",
            "version": "3.8.10",
            "mimetype": "text/x-python",
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "pygments_lexer": "ipython3",
            "nbconvert_exporter": "python",
            "file_extension": ".py"
        }
    },
    "nbformat_minor": 2,
    "nbformat": 4,
    "cells": [
        {
            "cell_type": "markdown",
            "source": [
                "Import Libraries"
            ],
            "metadata": {
                "azdata_cell_guid": "8b20f7bf-39cd-47e4-951c-9109f7b9a6b4"
            },
            "attachments": {}
        },
        {
            "cell_type": "code",
            "source": [
                "import pandas as pd\r\n",
                "import sqlalchemy \r\n",
                "from sqlalchemy.orm import Session\r\n",
                "from sqlalchemy import create_engine\r\n",
                "import pyodbc"
            ],
            "metadata": {
                "language": "python",
                "azdata_cell_guid": "8c41a381-0677-42a0-b5f0-d4eb86c63eb7"
            },
            "outputs": [],
            "execution_count": 186
        },
        {
            "cell_type": "markdown",
            "source": [
                "## using SQLalchemy\r\n",
                "\r\n",
                ""
            ],
            "metadata": {
                "azdata_cell_guid": "aa5d660a-076e-40b2-b0c8-9c01cc61d2b5"
            },
            "attachments": {}
        },
        {
            "cell_type": "code",
            "source": [
                "# Using sqlalchemy\r\n",
                "server = 'DABAS\\SQLEXPRESS'\r\n",
                "database = 'ChurnDataset'\r\n",
                "driver = 'SQL Server'\r\n",
                "connection = f\"mssql://@{server}/{database}?driver={'SQL Server'}\"\r\n",
                "engine = create_engine(connection)\r\n",
                "connect = engine.connect()\r\n",
                ""
            ],
            "metadata": {
                "language": "python",
                "azdata_cell_guid": "5b527439-74e0-4153-b92e-3cce670bc0cf"
            },
            "outputs": [],
            "execution_count": 187
        },
        {
            "cell_type": "code",
            "source": [
                "#read data and covert to df\r\n",
                "df = pd.read_sql(\r\n",
                "      'SELECT * FROM Data',\r\n",
                "  engine,\r\n",
                "  index_col='customer_id')\r\n",
                "df"
            ],
            "metadata": {
                "language": "python",
                "azdata_cell_guid": "e0c17028-1f0e-4e08-9990-610874e840ad"
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "             credit_score  country  gender  age  tenure        balance  \\\ncustomer_id                                                              \n15634602              619   France  Female   42       2       0.000000   \n15647311              608    Spain  Female   41       1   83807.859375   \n15619304              502   France  Female   42       8  159660.796875   \n15701354              699   France  Female   39       1       0.000000   \n15737888              850    Spain  Female   43       2  125510.820312   \n...                   ...      ...     ...  ...     ...            ...   \n15606229              771   France    Male   39       5       0.000000   \n15569892              516   France    Male   35      10   57369.609375   \n15584532              709   France  Female   36       7       0.000000   \n15682355              772  Germany    Male   42       3   75075.312500   \n15628319              792   France  Female   28       4  130142.789062   \n\n             products_number  credit_card  active_member  estimated_salary  \\\ncustomer_id                                                                  \n15634602                   1         True           True     101348.882812   \n15647311                   1        False           True     112542.578125   \n15619304                   3         True          False     113931.570312   \n15701354                   2        False          False      93826.632812   \n15737888                   1         True           True      79084.101562   \n...                      ...          ...            ...               ...   \n15606229                   2         True          False      96270.640625   \n15569892                   1         True           True     101699.773438   \n15584532                   1        False           True      42085.578125   \n15682355                   2         True          False      92888.523438   \n15628319                   1         True          False      38190.781250   \n\n             churn  \ncustomer_id         \n15634602      True  \n15647311     False  \n15619304      True  \n15701354     False  \n15737888     False  \n...            ...  \n15606229     False  \n15569892     False  \n15584532      True  \n15682355      True  \n15628319     False  \n\n[10000 rows x 11 columns]",
                        "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>credit_score</th>\n      <th>country</th>\n      <th>gender</th>\n      <th>age</th>\n      <th>tenure</th>\n      <th>balance</th>\n      <th>products_number</th>\n      <th>credit_card</th>\n      <th>active_member</th>\n      <th>estimated_salary</th>\n      <th>churn</th>\n    </tr>\n    <tr>\n      <th>customer_id</th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>15634602</th>\n      <td>619</td>\n      <td>France</td>\n      <td>Female</td>\n      <td>42</td>\n      <td>2</td>\n      <td>0.000000</td>\n      <td>1</td>\n      <td>True</td>\n      <td>True</td>\n      <td>101348.882812</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>15647311</th>\n      <td>608</td>\n      <td>Spain</td>\n      <td>Female</td>\n      <td>41</td>\n      <td>1</td>\n      <td>83807.859375</td>\n      <td>1</td>\n      <td>False</td>\n      <td>True</td>\n      <td>112542.578125</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>15619304</th>\n      <td>502</td>\n      <td>France</td>\n      <td>Female</td>\n      <td>42</td>\n      <td>8</td>\n      <td>159660.796875</td>\n      <td>3</td>\n      <td>True</td>\n      <td>False</td>\n      <td>113931.570312</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>15701354</th>\n      <td>699</td>\n      <td>France</td>\n      <td>Female</td>\n      <td>39</td>\n      <td>1</td>\n      <td>0.000000</td>\n      <td>2</td>\n      <td>False</td>\n      <td>False</td>\n      <td>93826.632812</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>15737888</th>\n      <td>850</td>\n      <td>Spain</td>\n      <td>Female</td>\n      <td>43</td>\n      <td>2</td>\n      <td>125510.820312</td>\n      <td>1</td>\n      <td>True</td>\n      <td>True</td>\n      <td>79084.101562</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>15606229</th>\n      <td>771</td>\n      <td>France</td>\n      <td>Male</td>\n      <td>39</td>\n      <td>5</td>\n      <td>0.000000</td>\n      <td>2</td>\n      <td>True</td>\n      <td>False</td>\n      <td>96270.640625</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>15569892</th>\n      <td>516</td>\n      <td>France</td>\n      <td>Male</td>\n      <td>35</td>\n      <td>10</td>\n      <td>57369.609375</td>\n      <td>1</td>\n      <td>True</td>\n      <td>True</td>\n      <td>101699.773438</td>\n      <td>False</td>\n    </tr>\n    <tr>\n      <th>15584532</th>\n      <td>709</td>\n      <td>France</td>\n      <td>Female</td>\n      <td>36</td>\n      <td>7</td>\n      <td>0.000000</td>\n      <td>1</td>\n      <td>False</td>\n      <td>True</td>\n      <td>42085.578125</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>15682355</th>\n      <td>772</td>\n      <td>Germany</td>\n      <td>Male</td>\n      <td>42</td>\n      <td>3</td>\n      <td>75075.312500</td>\n      <td>2</td>\n      <td>True</td>\n      <td>False</td>\n      <td>92888.523438</td>\n      <td>True</td>\n    </tr>\n    <tr>\n      <th>15628319</th>\n      <td>792</td>\n      <td>France</td>\n      <td>Female</td>\n      <td>28</td>\n      <td>4</td>\n      <td>130142.789062</td>\n      <td>1</td>\n      <td>True</td>\n      <td>False</td>\n      <td>38190.781250</td>\n      <td>False</td>\n    </tr>\n  </tbody>\n</table>\n<p>10000 rows × 11 columns</p>\n</div>"
                    },
                    "metadata": {},
                    "execution_count": 188,
                    "output_type": "execute_result"
                }
            ],
            "execution_count": 188
        },
        {
            "cell_type": "code",
            "source": [
                "## Query specific results\r\n",
                "df_country = pd.read_sql(\r\n",
                "      '''select country,count(*) as TOTAL_CUSTOMERS\r\n",
                "from data\r\n",
                "group by country\r\n",
                "ORDER BY TOTAl_CUSTOMERS DESC''',\r\n",
                "  engine)\r\n",
                "df_country\r\n",
                "\r\n",
                ""
            ],
            "metadata": {
                "azdata_cell_guid": "a054640e-7ba3-4f49-a453-75bfd52ed250",
                "language": "python"
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "   country  TOTAL_CUSTOMERS\n0   France             5014\n1  Germany             2509\n2    Spain             2477",
                        "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>country</th>\n      <th>TOTAL_CUSTOMERS</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>France</td>\n      <td>5014</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Germany</td>\n      <td>2509</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Spain</td>\n      <td>2477</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
                    },
                    "metadata": {},
                    "execution_count": 189,
                    "output_type": "execute_result"
                }
            ],
            "execution_count": 189
        },
        {
            "cell_type": "markdown",
            "source": [
                "\n",
                "## using pyodbc\n",
                ""
            ],
            "metadata": {
                "azdata_cell_guid": "ce5a3460-6a24-4cce-9c76-670b17c8eb34"
            },
            "attachments": {}
        },
        {
            "cell_type": "code",
            "source": [
                "\r\n",
                "connection = pyodbc.connect('Trusted_Connection=yes', \r\n",
                "                     driver = '{ODBC Driver 17 for SQL Server}',\r\n",
                "                     server = 'DABAS\\SQLEXPRESS', \r\n",
                "                     database = 'ChurnDataset')\r\n",
                ""
            ],
            "metadata": {
                "azdata_cell_guid": "3b0bd6be-5c92-4d50-8ac0-f06a7605d2bd",
                "language": "python"
            },
            "outputs": [],
            "execution_count": 190
        },
        {
            "cell_type": "code",
            "source": [
                "# get column names and type\r\n",
                "\r\n",
                "query= \"SELECT * FROM Data\"\r\n",
                "cursor = connection.cursor()\r\n",
                "cursor.execute(query)\r\n",
                "column_names = [desc[0] for desc in cursor.description]\r\n",
                "column_types = [desc[1] for desc in cursor.description]\r\n",
                "print(column_names)\r\n",
                "print(column_types)\r\n",
                "\r\n",
                ""
            ],
            "metadata": {
                "language": "python",
                "azdata_cell_guid": "28148064-5e14-4d56-8b28-b3375bbcd29b"
            },
            "outputs": [
                {
                    "name": "stdout",
                    "text": "['customer_id', 'credit_score', 'country', 'gender', 'age', 'tenure', 'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary', 'churn']\n[<class 'int'>, <class 'int'>, <class 'str'>, <class 'str'>, <class 'int'>, <class 'int'>, <class 'float'>, <class 'int'>, <class 'bool'>, <class 'bool'>, <class 'float'>, <class 'bool'>]\n",
                    "output_type": "stream"
                }
            ],
            "execution_count": 191
        },
        {
            "cell_type": "code",
            "source": [
                "#combine these\r\n",
                "for each in cursor.description:\r\n",
                "    print(each[0:2])"
            ],
            "metadata": {
                "language": "python",
                "azdata_cell_guid": "38564e0e-8b6a-46c2-9a13-7ca1cf6351b4"
            },
            "outputs": [
                {
                    "name": "stdout",
                    "text": "('customer_id', <class 'int'>)\n('credit_score', <class 'int'>)\n('country', <class 'str'>)\n('gender', <class 'str'>)\n('age', <class 'int'>)\n('tenure', <class 'int'>)\n('balance', <class 'float'>)\n('products_number', <class 'int'>)\n('credit_card', <class 'bool'>)\n('active_member', <class 'bool'>)\n('estimated_salary', <class 'float'>)\n('churn', <class 'bool'>)\n",
                    "output_type": "stream"
                }
            ],
            "execution_count": 192
        },
        {
            "cell_type": "code",
            "source": [
                "#sinmpler and easier way of doing this\r\n",
                "df_2 = pd.read_sql( \"SELECT * FROM Data\",connection)\r\n",
                "df_2.dtypes"
            ],
            "metadata": {
                "azdata_cell_guid": "9e01edac-bc60-4818-9f11-0bdc2aaf7e75",
                "language": "python"
            },
            "outputs": [
                {
                    "name": "stderr",
                    "text": "<ipython-input-194-6f3a47368e2f>:2: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.\n  df_2 = pd.read_sql( \"SELECT * FROM Data\",connection)\n",
                    "output_type": "stream"
                },
                {
                    "data": {
                        "text/plain": "customer_id           int64\ncredit_score          int64\ncountry              object\ngender               object\nage                   int64\ntenure                int64\nbalance             float64\nproducts_number       int64\ncredit_card            bool\nactive_member          bool\nestimated_salary    float64\nchurn                  bool\ndtype: object"
                    },
                    "metadata": {},
                    "execution_count": 194,
                    "output_type": "execute_result"
                }
            ],
            "execution_count": 194
        },
        {
            "cell_type": "code",
            "source": [
                "cursor = connection.cursor()\r\n",
                "cursor.execute(query3)\r\n",
                "a= cursor.fetchall()\r\n",
                "print(a)"
            ],
            "metadata": {
                "language": "python",
                "azdata_cell_guid": "371458e2-5e23-406d-ae02-6c3519683067"
            },
            "outputs": [
                {
                    "name": "stdout",
                    "text": "[]\n",
                    "output_type": "stream"
                }
            ],
            "execution_count": 170
        },
        {
            "cell_type": "code",
            "source": [
                "#no of customers countrywise\r\n",
                "\r\n",
                "df_pydoc = pd.read_sql( '''select country,count(*) as TOTAL_CUSTOMERS\r\n",
                "from data\r\n",
                "group by country\r\n",
                "ORDER BY TOTAl_CUSTOMERS DESC''',connection)\r\n",
                "df_pydoc\r\n",
                ""
            ],
            "metadata": {
                "language": "python",
                "azdata_cell_guid": "68d3e00d-55fd-4585-a8bf-41ed6f1a53d2",
                "tags": []
            },
            "outputs": [
                {
                    "name": "stderr",
                    "text": "<ipython-input-173-925ac53c70da>:3: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.\n  df_pydoc = pd.read_sql( '''select country,count(*) as TOTAL_CUSTOMERS\n",
                    "output_type": "stream"
                },
                {
                    "data": {
                        "text/plain": "   country  TOTAL_CUSTOMERS\n0   France             5014\n1  Germany             2509\n2    Spain             2477",
                        "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>country</th>\n      <th>TOTAL_CUSTOMERS</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>France</td>\n      <td>5014</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Germany</td>\n      <td>2509</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Spain</td>\n      <td>2477</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
                    },
                    "metadata": {},
                    "execution_count": 173,
                    "output_type": "execute_result"
                }
            ],
            "execution_count": 173
        }
    ]
}