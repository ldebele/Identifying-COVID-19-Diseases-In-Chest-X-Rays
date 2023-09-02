import os, sys, glob, random, shutil


BASE_DIR = './data/dataset_1'

COVID_DIR = os.path.join(BASE_DIR, 'data/1')
NO_COVID_DIR = os.path.join(BASE_DIR, 'data/0')


def train_test_split(dir, images, cls, mode):
    """
        Args:
            dir: str        -> location of raw dataset
            images: list    -> list of selected images.
            mode: str       -> types of sets [train, val, test]
    """
    MODE_DIR = os.path.join(BASE_DIR, f"{mode}/{cls}")
    # create directory if not created.
    os.makedirs(MODE_DIR, exist_ok=True)

    # copy the resampled file into the mode directory
    for image in images:
        origin = os.path.join(dir, image)
        destination = os.path.join(MODE_DIR, image)
        shutil.copy(origin, destination)
    


if __name__ == '__main__':


    for cls, dir in enumerate([COVID_DIR, NO_COVID_DIR]):
        random.seed(42)
        sample = sys.argv[1]
        images = random.sample(os.listdir(dir), int(sample))

        # calculate split size.
        train_size = int(len(images)*0.7)
        val_size = int(len(images)*0.15)

        # split the datasets into train, val and test sets.
        train_sets = images[:train_size]
        val_sets = images[train_size:train_size+val_size]
        test_sets = images[train_size+val_size:]

        #
        train_test_split(dir, train_sets, cls, mode="train",)
        train_test_split(dir, val_sets, cls, mode='val')
        train_test_split(dir, test_sets, cls, mode='test')

