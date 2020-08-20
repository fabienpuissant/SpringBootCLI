
nameEntity = input("Name of the entity to create : " )

tableName = input("Name of the table : ")

packageName = input("name of the package : ")

print(nameEntity)

entityFields = []
typeFields = []

propertyAgain = True

while(propertyAgain):
    field = input("Name of the property : ( o to cancel ) ")
    
    if(field == "o" or field == "O"):
        propertyAgain = False
    else :
        typeField = input("Type of the property : ")
        entityFields.append(field)
        typeFields.append(typeField)

#Generating the Entity file
fichier = open(nameEntity + "Entity.java", "w")

#Generate imports, headers and id field
fichier.write("package " + packageName + ";\n"
                "import javax.persistence.Column;\n" +
                "import javax.persistence.Entity;\n"+
                "import javax.persistence.GeneratedValue;\n"+
                "import javax.persistence.GenerationType;\n"+
                "import javax.persistence.Id;\n"+
                "import javax.persistence.Table;\n\n" + 
                "@Entity\n" + 
                "@Table(name = \""+ tableName + "\")\n\n" + 
                "public class " + nameEntity + "Entity {\n\n"+
                "\t@Id\n"+
                "\t@GeneratedValue(strategy=GenerationType.AUTO)\n"+
                "\tprivate Integer id;\n\n"
            )

#Generate the properties
for i in range(len(entityFields)):
    fichier.write(
        "\t@Column\n" + 
        "\tprivate " + typeFields[i] + " " + entityFields[i] + ";\n\n"
        )

#Generate construcor
fichier.write("\tpublic " + nameEntity + "Entity () { \n\n    \t}\n\n")

#Generate getter and setters
for i in range(len(entityFields)):
    typeField = typeFields[i]
    entityField = entityFields[i]
    entityCamelCase = entityFields[i][0].title()
    for j in range(1, len(entityFields[i])):
        entityCamelCase = entityCamelCase + entityFields[i][j] 
    fichier.write("\tpublic " + typeField + " get" + entityCamelCase + "() {\n" +
                    "\t\treturn " + entityField + ";\n" +
                    "\t}\n\n" + 
                    "\tpublic void set" + entityCamelCase + "(" + typeField + " " + entityField + ") {\n" + 
                    "\t\tthis." + entityField + " = " + entityField + ";\n" + 
                    "\t} \n\n"    
                )
fichier.write("}")
fichier.close()
    

#Generating the repository
fichier = open(nameEntity +"Repository.java", "w")

fichier.write("package " + packageName + ";\n"
                "import org.springframework.data.repository.CrudRepository;\n" +
                "import java.util.List;\n" +
                "import org.springframework.stereotype.Repository;\n" + 
                "import "+ packageName + "." + nameEntity + "Entity" + ";\n\n"+
                "@Repository \n" +
                "public interface " + nameEntity + "Repository extends CrudRepository<" + nameEntity + "Entity, Integer> {\n\n" + 
                "\t public List<" + nameEntity + "Entity> findAll();\n\n" + 
                "\t public " + nameEntity + "Entity findById(int id);\n\n" 
            )

#Writing find by property functions
for i in range(len(entityFields)):
    entityField = entityFields[i][0].title()
    for j in range(1, len(entityFields[i])):
        entityField = entityField + entityFields[i][j]  
    fichier.write("\tpublic " + nameEntity + "Entity findOneBy" + entityField + "(" + typeFields[i] + " " + entityFields[i] + ");\n\n")

fichier.write("}")

fichier.close()

#Generating the service
fichier = open(nameEntity +"Service.java", "w")
repositoryVar =  nameEntity.lower() + "Repository"

fichier.write("package " + packageName + ";\n"
                "import org.springframework.beans.factory.annotation.Autowired;\n" + 
                "import java.util.List;\n" +
                "import org.springframework.stereotype.Service;\n\n" + 
                "@Service\n" + 
                "public class " + nameEntity + "Service {\n\n"
                "\t@Autowired\n" +
                "\tprivate " + nameEntity + "Repository " + nameEntity.lower() + "Repository;\n\n"

                "\tpublic List<" + nameEntity + "Entity> getAll() {\n" + 
                "\t\treturn " + repositoryVar + ".findAll();" + 
                "\t}\n\n"

                "\tpublic "  + nameEntity + "Entity get" + nameEntity + "ById(int id) {\n" + 
                "\t\treturn " + repositoryVar + ".findById(id);\n"
                "\t}\n\n"

                "\tpublic void add" + nameEntity + "(" + nameEntity + "Entity " + nameEntity.lower() + ") {\n" + 
                "\t\t" + repositoryVar +".save(" + nameEntity.lower() + ");\n" + 
                "\t}\n\n"

                "\tpublic void update" + nameEntity + "(" + nameEntity + "Entity " + nameEntity.lower() + ") {\n" + 
                "\t\t" + repositoryVar +".save(" + nameEntity.lower() + ");\n" + 
                "\t}\n\n"

                "\tpublic void delete" + nameEntity + "(int id) {\n" + 
                "\t\t" + repositoryVar +".delete(" + repositoryVar + ".findById(id));\n" + 
                "\t}\n\n"
            
            )


#find by properties
for i in range(len(entityFields)):
    entityField = entityFields[i][0].title()
    for j in range(1, len(entityFields[i])):
        entityField = entityField + entityFields[i][j]  
    fichier.write("\tpublic " + nameEntity + "Entity get" + nameEntity + "By" + entityField +"(" + typeFields[i] + " " + entityFields[i] + ") {\n" +
                "\t\treturn "+ repositoryVar + ".findOneBy" + entityField + "(" + entityFields[i] + ");\n" + 
                "\t}\n\n"
    )


fichier.write("}")
fichier.close()

fichier = open(nameEntity +"RestController.java", "w")
serviceVar = nameEntity.lower() + "Service"
path = nameEntity + "Service"

fichier.write("package " + packageName + ";\n"
                "import org.springframework.http.MediaType;\n" +
                "import org.springframework.beans.factory.annotation.Autowired;\n" +
                "import org.springframework.web.bind.annotation.GetMapping;\n" + 
                "import org.springframework.web.bind.annotation.PutMapping;\n" + 
                "import org.springframework.web.bind.annotation.DeleteMapping;\n" + 
                "import org.springframework.web.bind.annotation.PathVariable;\n" +  
                "import org.springframework.web.bind.annotation.PostMapping;\n" +  
                "import org.springframework.web.bind.annotation.RequestBody;\n" + 
                "import org.springframework.web.bind.annotation.RestController;\n\n" +   
                "@RestController\n" + 
                "public class " + nameEntity + "RestController {\n\n"+
                "\t@Autowired\n" +
                "\tprivate " + nameEntity + "Service " + nameEntity.lower() + "Service;\n\n"+

                "\t@GetMapping(\"" + path + "/{id}\")\n" + 
                "\tpublic " + nameEntity + "Entity getUserById(@PathVariable int id) { \n"+
                "\t\t return " + serviceVar + ".get" + nameEntity + "ById(id);" +
                "\t}\n\n"

                "\t@PostMapping(value=\"" + path + "/add" + nameEntity + "\", consumes=MediaType.APPLICATION_JSON_VALUE)\n"+
                "\tpublic void add" + nameEntity + "(@RequestBody " + nameEntity + "Entity " + nameEntity.lower() +") { \n"+
                "\t\t" + serviceVar + ".add" + nameEntity + "("+ nameEntity.lower() +");\n" + 
                "\t}\n\n"

                "\t@DeleteMapping(\"" + path + "/delete/{id}" + "\")\n"+
                "\tpublic void deleteById" + nameEntity + "(@PathVariable int id) { \n"+
                "\t\t" + serviceVar + ".delete" + nameEntity + "(id);\n" + 
                "\t}\n\n"
            
            )
fichier.write("}")
fichier.close()



