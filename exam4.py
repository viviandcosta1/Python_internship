school = {
    "student1":{
        "name" : "vvn",
        "roll no" : 101
    },
    "student2":{
        "name" : "suhas",
        "roll no" : 102
    },
    "student2":{
        "name" : "shreyash",
        "roll no" : 103
    },
    "student3":{
        "name" : "shavia",
        "roll no" : 105
    },
    "student4":{
        "name" : "sona",
        "roll no" : 106
    },
    "student5":{
        "name" : "vvn",
        "roll no" : 107
    },
    "student8":{
        "name" : "yakee",
        "roll no" : 108
    }

}
school.update({"name" : "priya","roll no":"104"})
school.pop("student2")
print(school)