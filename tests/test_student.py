from school_schedule.student import Student

def test_adding_one_class_increases_class_length():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = Student(name, grade, classes)

    # Act
    ellis.add_class("Pottery")

    # Assert
    assert ellis.classes == ["Painting", "Pottery"]

def test_input_for_classes_is_alpha():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = Student(name, grade, classes)

    # Act
    class_input_not_alpha = ellis.add_class("943")

    # Assert
    assert class_input_not_alpha is None