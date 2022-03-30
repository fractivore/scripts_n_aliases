import sys
chosen_name=sys.argv[1]
code=f"""
#include \"{chosen_name}.h\"

//test driver code for {chosen_name}
int main(){



}
"""
print(code)
