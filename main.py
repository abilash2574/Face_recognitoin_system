import compareface as cf
import data_Register as dr


if __name__ == '__main__':
    # dir_path = 'Images'
    # dr.start_data_registry(dir_path)
    capture1 = cf.CompareFace()
    capture1.compare_face()
