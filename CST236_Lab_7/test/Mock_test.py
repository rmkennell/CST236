
from unittest import TestCase

import mock
from mock import patch
from test.plugins.ReqTracer import requirements

from source.git_utils import get_git_file_info, is_file_in_repo, has_untracked_files, get_file_info, get_repo_branch, get_repo_url

class TestFilePath(TestCase):
    """
    Tests the validity of a filepath
    """
    @requirements(['#00100'])
    @patch('subprocess.Popen')
    def test_file_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('output', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = is_file_in_repo("requirementTest.txt")
        self.assertTrue(result)
        self.assertTrue(mock_subproc_popen.called)

    # does not exist
    #@requirements(['#00100'])
    #@patch('subprocess.Popen')
    #def test_file_path(self, mock_subproc_popen):
    #    process_mock = mock.Mock()
    #    attrs = {'communicate.return_value': ('output', '')}
    #    process_mock.configure_mock(**attrs)
    #    mock_subproc_popen.return_value = process_mock
    #    x = is_file_in_repo("/Users/ryankennell/Desktop/label3.pdf")
    #    self.assertEqual(x, "No")
    #    self.assertTrue(mock_subproc_popen.called)

    # Is a dirty repo
    @requirements(['#00101'])
    @patch('subprocess.Popen')
    def test_status_of_file(self, mock_subproc_popen):
        """
        Tests the status of a file
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('/', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = get_git_file_info("requirementTest.txt")
        self.assertEquals(result, 'requirementTest.txt is a dirty repo')
        self.assertTrue(mock_subproc_popen.called)

    # Is up to Date
    @requirements(['#00101'])
    @patch('subprocess.Popen')
    def test_status_of_file_up_to_date(self, mock_subproc_popen):
        """
        Checks the ability to test of file is up to date
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = get_git_file_info("requirementTest.txt")
        self.assertEquals(result, 'requirementTest.txt is up to date')
        self.assertTrue(mock_subproc_popen.called)

    # Has been modified locally
    ##@requirements(['#00101'])
    #@patch('subprocess.Popen')
    #def test_status_of_file_modified(self, mock_subproc_popen):
    #    process_mock = mock.Mock()
     #   attrs = {'communicate.return_value': ('/Users/ryankennell/Desktop/label.pdf', '')}
     #   process_mock.configure_mock(**attrs)
     #   mock_subproc_popen.return_value = process_mock
     #   x = get_git_file_info("/Users/ryankennell/Desktop/label.pdf")
     #   self.assertEquals(x, 'label.pdf has been modified locally')
      #  self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_untracked_files(self, mock_subproc_popen):
        """
        Tests the untracted files
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('requirementTest.txt', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = has_untracked_files("requirementTest.txt")
        self.assertTrue(result)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_is_absolute_path(self, mock_subproc_popen):
        """
        checks if absolute path
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('requirementTest.txt', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = is_file_in_repo("requirementTest.txt")
        self.assertTrue(result)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_get_repo_url(self, mock_subproc_popen):
        """
        Tests the get repo url
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('requirementTest.txt', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = get_repo_url("requirementTest.txt")
        self.assertTrue(result)
        self.assertTrue(mock_subproc_popen.called)

    # Has not been checked in
    #@requirements(['#00101'])
    #@patch('subprocess.Popen')
    #def test_absolute_file_path(self, mock_subproc_popen):
    #    process_mock = mock.Mock()
    #    attrs = {'communicate.return_value': ('/Users/ryankennell/Desktop/label.pdf', '')}
    #    process_mock.configure_mock(**attrs)
    #    mock_subproc_popen.return_value = process_mock
    #    x = get_git_file_info("/Users/ryankennell/Desktop/label.pdf")
    #    self.assertEqual(x, 'label.pdf has been not been checked in')
    #    self.assertTrue(mock_subproc_popen.called)

    # Get file info
    @requirements(['#00102'])
    @patch('subprocess.Popen')
    def test_absolute_file_path2(self, mock_subproc_popen):
        """
        test absolute path 2
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('test', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = get_file_info('requirementTest.txt', True)
        self.assertEqual(result, 'test')
        self.assertTrue(mock_subproc_popen.called)

    # Get repo branch
    @requirements(['#00103'])
    @patch('subprocess.Popen')
    def test_absolute_file_path3(self, mock_subproc_popen):
        """
        Tests the absolute filepath
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('requirementTest.txt', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = get_repo_branch("requirementTest.txt")
        self.assertTrue(result)
        self.assertTrue(mock_subproc_popen.called)


    @requirements(['#00103'])
    @patch('subprocess.Popen')
    def test_get_git_file_exce(self, mock_subproc_popen):
        """
        Tests teh get git file exception
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        self.assertRaisesRegexp(Exception, "")


