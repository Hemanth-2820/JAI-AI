import re
import os

def main():
    file_path = r'src\pages\Services\categoryData.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    expansions = [
        " Our dedicated team ensures highly scalable, secure, and customized implementation tailored perfectly to your unique business requirements.",
        " We leverage industry-leading best practices to deliver robust, high-performance solutions that drive measurable growth and efficiency.",
        " Designed with future-proofing in mind, this approach guarantees seamless integration, maximum reliability, and an exceptional user experience.",
        " Through advanced methodologies and precise execution, we transform complex challenges into streamlined, user-friendly digital assets."
    ]
    
    count = 0
    def replacer(match):
        nonlocal count
        original_desc = match.group(1)
        # Prevent double-expanding if run multiple times
        if " Our dedicated" in original_desc or " We leverage" in original_desc or " Designed with" in original_desc or " Through advanced" in original_desc:
            return match.group(0)
            
        expansion = expansions[count % len(expansions)]
        count += 1
        new_desc = original_desc.strip()
        if not new_desc.endswith('.'):
            new_desc += '.'
        new_desc += expansion
        return f'"desc": "{new_desc}"'

    new_content = re.sub(r'"desc":\s*"([^"]+)"', replacer, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully expanded {count} descriptions in categoryData.js")

if __name__ == "__main__":
    main()
