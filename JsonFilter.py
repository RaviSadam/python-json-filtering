

# import json


# # #USING list Comprehension

# # #JSON String
# # jsonString="""[
# #   {
# #     "name": "Ravi Kumar",
# #     "age": 28,
# #     "city": "Mumbai",
# #     "gender": "Male",
# #     "occupation": "Software Engineer"
# #   },
# #   {
# #     "name": "Aishwarya Singh",
# #     "age": 32,
# #     "city": "Delhi",
# #     "gender": "Female",
# #     "occupation": "Marketing Manager"
# #   },
# #   {
# #     "name": "Ramakrishna",
# #     "age": 35,
# #     "city": "Ahmedabad",
# #     "gender": "Male",
# #     "occupation": "Business Owner"
# #   },
# #   {
# #     "name": "Priya Sharma",
# #     "age": 26,
# #     "city": "Bangalore",
# #     "gender": "Female",
# #     "occupation": "Data Scientist"
# #   }
# # ]"""


# # #converting JSON String to Python object
# # jsonObject=json.loads(jsonString)

# # #filtering data using list Comprehension
# # filteredData=[ person for person in jsonObject if person['age']>25 and person['age']<30 and person['gender'] == 'Male' ]

# # #converting the python object into JSON String
# # filteredJsonData=json.dumps(filteredData)

# # #printing the data
# # print(filteredJsonData)



# import pandas
# from pandas import json_normalize

# #Using Pandas

# #File Ojects
# jsonFile=open("data.json","r")

# #JSON To Python Object
# jsonData=json.loads(jsonFile.read())


# #creating data frame
# dataFrame=json_normalize(jsonData)

# #print data Frame
# print(dataFrame)
# print("\n")


# #filtering dataframe
# filteredData=dataFrame.loc[(dataFrame['age']>30) & (dataFrame['address.city']=="City1"),['name','age','address.city','address.zipcode']]

# #print filtered dataframe
# print(filteredData)
# print("\n")

# # DataFrame TO JSON Objcet
# filteredJsonData=filteredData.to_json(orient='records')
# print(filteredJsonData)



from  jsonpath_ng.ext import parse

# Sample JSON data representing a list of people
data_dict = {
    "people": [
        {"name": "John Doe", "age": 30, "city": "New York"},
        {"name": "Jane Smith", "age": 25, "city": "Los Angeles"},
        {"name": "Bob Johnson", "age": 35, "city": "Chicago"}
    ]
}

# Define a JSONPath expression for filtering
path_expr = parse('$.people[?(@.age >= 30)].name')

# Apply the expression to the data
matches = [people.value for people in path_expr.find(data_dict)]

# Display the 
print(matches)