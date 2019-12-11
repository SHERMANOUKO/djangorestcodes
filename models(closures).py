#a model class that renames four images to 1.jpg, 2.jopg, 3.jpg, 4.jpg using closures concept

#without closures / first class functions concept
class Student(models.Model):
    def _image_file_name_one(instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (
	    1,
            ext
        )
        return filename

    def _image_file_name_two(instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (
	    2,
            ext
        )
        return filename

    def _image_file_name_three(instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (
	    3,
            ext
        )
        return filename

    def _image_file_name_four(instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (
	    4,
            ext
        )
        return filename
    
    studentID = models.AutoField(primary_key=True)
    studentClass = models.CharField(max_length=10)
    studentDorm = models.ForeignKey(Dormitories, on_delete=models.SET_NULL, null=True)
    studentPhotoOne = models.ImageField(storage=MediaStorage(), upload_to=_image_file_name_one)
    studentPhotoTwo = models.ImageField(storage=MediaStorage(), upload_to=_image_file_name_two)
    studentPhotoThree = models.ImageField(storage=MediaStorage(), upload_to=_image_file_name_three)
    studentPhotoFour = models.ImageField(storage=MediaStorage(), upload_to=_image_file_name_four)

#with closures / first class functions concept
class Student(models.Model):
    def _image_file_name(image_number):
        def _image_specific_file_name(instance, filename):
            ext = filename.split('.')[-1]
            filename = '%s.%s' % (
		        str(image_number),
                ext
            )
            return filename
        return _image_specific_file_name
    
    studentID = models.AutoField(primary_key=True)
    studentClass = models.CharField(max_length=10)
    studentDorm = models.ForeignKey(Dormitories, on_delete=models.SET_NULL, null=True)
    studentPhotoOne = models.ImageField(storage=MediaStorage(), upload_to=_image_file_name(1))
    studentPhotoTwo = models.ImageField(storage=MediaStorage(), upload_to=_image_file_name(2))
    studentPhotoThree = models.ImageField(storage=MediaStorage(), upload_to=_image_file_name(3))
    studentPhotoFour = models.ImageField(storage=MediaStorage(), upload_to=_image_file_name(4))

