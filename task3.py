import pandas as pd

def read_csv(file_path):
    '''Reading csv file from given file path.'''

    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def calculate_average_grade(df):
    '''This function calculates average grade for given dataframe.'''

    average_grade = df['language.grade'].mean()
    highest_grade_student = df.loc[df['language.grade'].idxmax()]
    return average_grade, highest_grade_student

def filter_students(df, min_grade=None, age_range=None):
    '''This function filters students based on min-grade and age-range provided'''

    if min_grade is not None:
        df = df[df['language.grade'] > min_grade]
    if age_range is not None:
        df = df[df['age'].between(age_range[0], age_range[1])]
    return df

def sort_students(df, sort_by='name', ascending=True):
    '''This function sort the dataframe based on sort_by column specified'''

    return df.sort_values(by=sort_by, ascending=ascending)

def write_to_csv(df, output_file):
    '''This function write a data to output csv file'''
    
    df.to_csv(output_file, index=False)
    print(f"Filtered and sorted data written to '{output_file}'.")

def main():
    input_file = 'src/student-dataset.csv'
    output_file = 'dest/student-data-output.csv'
    df = read_csv(input_file)
    
    if df is not None:
        average_grade, highest_grade_student = calculate_average_grade(df)
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Highest Grade Student: {highest_grade_student['name']} with grade {highest_grade_student['language.grade']}")

        min_grade = float(input("Enter minimum grade to filter students: ") or 0)
        age_min = input("Enter minimum age : ")
        age_max = input("Enter maximum age : ")
        age_range = (int(age_min), int(age_max)) if age_min and age_max else None
        
        filtered_students = filter_students(df, min_grade, age_range)
        print(f"Filtered Students:\n{filtered_students}")

        sort_by = input("Enter the column to sort by (name/age/grade, default is name): ") or 'name'
        ascending = input("Sort in ascending order? (yes/no, default is yes): ").strip().lower() in ['yes', 'y', '']
        sorted_students = sort_students(filtered_students, sort_by, ascending)

        write_to_csv(sorted_students, output_file)

if __name__ == "__main__":
    main()
    print("task Completed")
