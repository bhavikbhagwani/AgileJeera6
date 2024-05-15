import unittest
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

    def test_play_sound(self):
        # Check if play_sound() method doesn't raise any exceptions
        self.sounds.play_sound(1)  # Playing a valid sound
        self.sounds.play_sound(100)  # Playing an invalid sound

    def test_stop_sound(self):
        # Check if stop_sound() method doesn't raise any exceptions
        self.sounds.stop_sound()

if __name__ == '__main__':
    unittest.main()
