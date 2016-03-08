
from unittest import TestCase
import mock

from plugins.ReqTracer import requirements
from source.main import Interface
from mock import patch
from source.git_utils import get_git_file_info, is_file_in_repo, has_untracked_files, get_file_info, get_repo_branch

class TestFilePath(TestCase):
    @requirements(['#00100'])
    @patch('subprocess.Popen')
    def test_file_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('output', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = is_file_in_repo("/Users/ryankennell/Desktop/label.pdf")
        self.assertTrue(x)
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
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('/Users/ryankennell/Desktop/', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_git_file_info("/Users/ryankennell/Desktop/label.pdf")
        self.assertEquals(x, 'label.pdf is a dirty repo')
        self.assertTrue(mock_subproc_popen.called)

    # Is up to Date
    @requirements(['#00101'])
    @patch('subprocess.Popen')
    def test_status_of_file_up_to_date(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_git_file_info("/Users/ryankennell/Desktop/label.pdf")
        self.assertEquals(x, 'label.pdf is up to date')
        self.assertTrue(mock_subproc_popen.called)

    # Has been modified locally
    @requirements(['#00101'])
    @patch('subprocess.Popen')
    def test_status_of_file_modified(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('/Users/ryankennell/Desktop/label.pdf', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_git_file_info("/Users/ryankennell/Desktop/label.pdf")
        self.assertEquals(x, 'label.pdf has been modified locally')
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_untracked_files(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('/Users/ryankennell/Desktop/label.pdf', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = has_untracked_files("/Users/ryankennell/Desktop/label.pdf")
        self.assertTrue(x)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_absolute_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('label.pdf', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = is_file_in_repo("/Users/ryankennell/Desktop/label.pdf")
        self.assertTrue(x)
        self.assertTrue(mock_subproc_popen.called)

    # Has not been checked in
    @requirements(['#00101'])
    @patch('subprocess.Popen')
    def test_absolute_file_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('/Users/ryankennell/Desktop/label.pdf', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_git_file_info("/Users/ryankennell/Desktop/label.pdf")
        self.assertEqual(x, 'label.pdf has been not been checked in')
        self.assertTrue(mock_subproc_popen.called)

    # Get file info
    @requirements(['#00102'])
    @patch('subprocess.Popen')
    def test_absolute_file_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('test', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_file_info('/Users/ryankennell/Desktop/label.pdf', True)
        self.assertEqual(x, '  ')
        self.assertTrue(mock_subproc_popen.called)

    # Get repo branch
    @requirements(['#00103'])
    @patch('subprocess.Popen')
    def test_absolute_file_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('Branch2', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_repo_branch("/Users/ryankennell/Desktop/label.pdf")
        self.assertEqual(x, 'Branch2')
        self.assertTrue(mock_subproc_popen.called)



    @requirements(['#00103'])
    @patch('subprocess.Popen')
    def test_absolute_file_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = "c"
        self.assertRaisesRegexp(Exception, "Path c does")
