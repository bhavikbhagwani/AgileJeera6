import unittest
from unittest.mock import MagicMock, patch
from sounds import Sounds  

class TestSounds(unittest.TestCase):
    def setUp(self):
        self.sounds = Sounds()

    def test_get_sound_url(self):
        # Test a valid sound number
        self.assertEqual(self.sounds.get_sound_url(1), "https://firebasestorage.googleapis.com/v0/b/aumeter-76464.appspot.com/o/meditation_1.mp3?alt=media&token=b22aaf93-2c27-4477-b96e-c351afdef7bc")
        # Test an invalid sound number
        self.assertIsNone(self.sounds.get_sound_url(100))

    def test_get_sound_name(self):
        # Test a valid sound number
        self.assertEqual(self.sounds.get_sound_name(1), "Breathing")
        # Test an invalid sound number
        self.assertIsNone(self.sounds.get_sound_name(100))

    @patch('requests.get')
    @patch('io.BytesIO')
    @patch('pygame.mixer.init')
    @patch('pygame.mixer.music.load')
    @patch('pygame.mixer.music.play')
    def test_play_sound(self, mock_play, mock_load, mock_init, mock_bytesio, mock_requests_get):
        # Mock response object
        mock_response = MagicMock()
        mock_response.content = b'some_audio_data'
        mock_requests_get.return_value = mock_response
        # Calling method
        self.sounds.play_sound(1)
        # Assertions
        mock_requests_get.assert_called_once_with(self.sounds.get_sound_url(1))
        mock_bytesio.assert_called_once_with(b'some_audio_data')
        mock_init.assert_called_once()
        mock_load.assert_called_once_with(mock_bytesio())
        mock_play.assert_called_once()

    @patch('pygame.mixer.music.stop')
    def test_stop_sound(self, mock_stop):
        # Calling method
        self.sounds.stop_sound()
        # Assertion
        mock_stop.assert_called_once()

if __name__ == '__main__':
    unittest.main()
