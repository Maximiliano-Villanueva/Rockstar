import sys, os
import unittest
import uuid
import shutil

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..','code')
sys.path.append(CODE_DIR)

from AppLoger import AppLoger


class FunctionsBlackBox(unittest.TestCase):

    """
    Blackbox testing for the functions file
    """

    def setUp(self):
        """
        create the logger
        """
        self._createLogger()
        


    def _createLogger(self):
        """
        create logger
        """
        #create guid
        uuid_session = uuid.uuid4()
        uuid_session_str = str(uuid_session)
        os.environ['app_guid'] = str(uuid_session)

        #creat apploger
        AppLoger.create_logger(guid = uuid_session_str, log_name=str(type(self)))
        self.logger = AppLoger.getLogger(uuid_session_str)

        
    def _createTempDir(self, dir_path, add_random_file = True):
        """
        create a temp dir
        """
        
        try:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            if add_random_file:
                file_name = 'file_test_{0}.txt'.format(str(uuid.uuid4()))
                with open(os.path.join(dir_path, file_name), 'w+') as file:
                    file.write('test')

                return file_name
        except:
            return False

        return True

            
    def test_black_box_zip(self):
        """
        test the zipping of a folder
        """
        from functions import zip_folder
        self._createLogger()
        
        
        #create temp dir and file
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        tmp_file_name = 'temp_file'
        temp_dir_path = os.path.join(ROOT_DIR, tmp_file_name)

        created = self._createTempDir(temp_dir_path)

        #if the folder has been created test the zip functionality
        if created:

            zip_path = zip_folder(temp_dir_path, tmp_file_name)
            self.assertGreater(os.path.getsize(zip_path), 0)
            shutil.rmtree(temp_dir_path)
            os.remove(zip_path)
        #abort test since the folder cannot be created
        else:
            self.assertEquals(0,1)
    
    def test_black_box_remove_file(self):
        """
        test the removal of the a empty directory
        """
        from functions import delete_non_empty_folder
        #create temp dir and file
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        tmp_file_name = 'temp_file'
        temp_dir_path = os.path.join(ROOT_DIR, tmp_file_name)

        created = self._createTempDir(temp_dir_path)

        #try to remove file
        delete_non_empty_folder(temp_dir_path)

        self.assertEqual(os.path.exists(temp_dir_path), 0)

unittest.main()