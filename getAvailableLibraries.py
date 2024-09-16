# list the available libraries available to the GenAI Builder
# place this script in a codeblock and set language to pythin
import importlib.metadata


packages = importlib.metadata.distributions()
package_list = []  # Array to hold the package entries

for pkg in packages:
    package_entry = f"{pkg.metadata['Name']}=={pkg.version}"
    package_list.append(package_entry)
	
return package_list
