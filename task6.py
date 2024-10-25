import re
from typing import Optional

def pattern_match_function(text: str, pattern: str) -> list[str]:
    """Function returns respective result for entered pattern"""

    matches:list[str] = re.findall(pattern, text)
    return matches


def capture_group_extraction(pattern: str, text: str) -> list[dict]:
    """Extracts information from the matched results using named capture groups."""

    matches = re.finditer(pattern, text)
    extracted_info:list[dict] = []
    for match in matches:
        extracted_info.append(match.groupdict())
    return extracted_info


def text_manipulation(pattern: Optional[str], replacement:Optional[str], text: str) -> str:
    """Replaces specific patterns in the text with desired replacements using regex."""

    if pattern and replacement:
        modified_text: str = re.sub(pattern, replacement, text)
        return modified_text
    
    print("\nNot modified : \n")
    return text

def validate_email(text: str) -> bool:
    """Function to validate user email"""

    pattern: str = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$"
    return re.match(pattern, text) is not None


def validate_number(text: str) -> bool:
    """FUnction to validate user contact number"""

    pattern:str = r"^(?:\+?[\s]?91[-\s]?)?(?:\(?\d{5}\)?[-\s]?)?\d{5}$"
    return re.match(pattern, text) is not None


def validate_date(date: str) -> bool:
    """Validates the date in format DD-MM-YYYY using regex."""

    pattern: str = r"^\d{2}-\d{2}-\d{4}$"
    return re.match(pattern, date) is not None


def split_text(pattern: str, text: str) -> list[str]:
    """Splits the text into specific components based on the regex pattern."""

    components: list[str] = re.split(pattern, text)
    return components


def join_text(components: list[str], separator: str) -> str:
    """Joins separate components into a single text with a separator."""

    return separator.join(components)


def main() -> None:
    text: str = """  On March 3, 2023, at 10:45 AM, an order was placed by user123 for 5 units of product 
            A25 priced at $19.99 each. This brought the total to $99.95. The payment was processed successfully, 
            and the order ID generated was ORD-4589. Later that day, another order came in from user456 for 3 
            units of product B10, costing $45.00 per unit, totaling $135.00. Payment was made using credit card 
            ending in 1234. The feedback from the users was overwhelmingly positive, with comments like 
            "Excellent service!" and "Fast delivery, thank you!"—which were recorded for reference."""

    while True:
        print("\nMenu")
        print("1. Pattern matching")
        print("2. Capture Group Extraction")
        print("3. Text Manipulation")
        print("4. Validation")
        print("5. Splitting")
        print("6. Join Components")
        print("7. Exit")
        selected_option: str|None = input("\nEnter option : ").strip() or '0'
        match selected_option:
            case '1':
                user_input_pattern: str | None = input("\nEnter regex pattern : ").strip() or '0'
                if user_input_pattern:
                    result = pattern_match_function(text, user_input_pattern)
                    print("\nMatched result : ", result)
                else:
                    print("\nInvalid pattern")

            case '2':
                pattern_with_groups: str | None = input("\nEnter a regex pattern with named capture groups (e.g., '(?P<name>\\w+)'): ").strip() or None
                if pattern_with_groups:
                    extracted_info = capture_group_extraction(pattern_with_groups, text)
                    print("Extracted Information:", extracted_info)
                else:
                    print("Invalid pattern")

            case '3':
                user_pattern:str | None = input("\nEnter regex pattern : ").strip() or None
                replacement: str | None = input("Enter replacement text here : ") or None
                replacement_result: str = text_manipulation(user_pattern, replacement, text)
                print(replacement_result)

            case'4':
                while True:
                    print("\n Validation Menu : ")
                    print("1. Email")
                    print("2. Phone")
                    print("3. Date")
                    print("4. Exit")
                    validation_selected: str = input("\nSelected option : ").strip() or '0'

                    match validation_selected:
                        case '1':
                            user_email: str | None = input("\nEnter email address to validate : ").strip() or None
                            if user_email:
                                email_result: bool = validate_email(user_email)
                                if email_result:
                                    print("\nvalid email")
                                else:
                                    print("\nNot valid email")
                            else:
                                print("\nEmail not entered")

                        case '2':
                            user_contact: str | None = input("\nEnter contact number to validate : ").strip() or None
                            if user_contact:
                                contact_result: bool = validate_number(user_contact)
                                if contact_result:
                                    print("\nvalid contact number")
                                else:
                                    print("\nNot valid contact number")
                            else:
                                print("\nContact number not entered")   

                        case '3':
                            user_date: str | None = input("\nEnter date : ").strip() or None
                            if user_date:
                                date_result: bool = validate_date(user_date)
                                if date_result:
                                    print("\nvalid date")
                                else:
                                    print("\nNot valid date")
                            else:
                                print("\nDate not entered")    

                        case '4':
                            break

                        case default:
                            print("\nEnter valid option")
            case '5':
                split_pattern: str | None = input("\nEnter a regex pattern for splitting the text: ").strip() or None
                if split_pattern:
                    components = split_text(split_pattern, text)
                    print("Split Components:", components)
                else:
                    print("\nregex pattern not entered")

            case '6':
                separator:str | None = input("\nEnter a separator : ") or None
                if separator:
                    split_pattern_separator:str | None = input("\nEnter a regex pattern for splitting the text: ").strip() or None
                    if split_pattern_separator:
                        splitted_components: list[str] = split_text(split_pattern_separator, text)
                        joined_text = join_text(splitted_components, separator)
                        print("\nJoined component : ", joined_text)
                else:
                    print("\nSeparator not entered")

            case '7':
                break
            case default:
                print("\nEnter valid option")


if __name__ == "__main__":
    main()
