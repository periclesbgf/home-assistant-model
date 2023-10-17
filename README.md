# home-assistant-model

To get started, please install all the libraries required to use this project with this command below.

```bash
pip install numpy tensorflow scipy sounddevice random
```

To run, go to `model/main.py` and at line 9, change this to your current directory, like this:

```python
loaded_model = models.load_model("../saved")
```

and then run the command below:

```bash
cd model
python3 main.py
```

to run the `main.py` file.

Note: sample_generator.py was used to record sound to fill our database.

This model was based on Tensorflow model, it will recognize one word each time. The audio file format is `.wav` in a 16000Hz. It was used 80% of data for trainning and 20% for validation. This model convert audio to spectrogram. Since spectrogram is an image, it is possible to use CNN (Convolutional Neuro Network) as a model. The model consists in two convolutional 2D CNN with ReLU activation, one layer for dimentionality reduction, one layer of dropout for overfiting reduction and the output model using the number of labels.