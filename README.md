# Image Search Engine
## See it live here!
https://zoesong.herokuapp.com/search

## If you want to run locally with your own Clarifai app
1. Change the Clarifai Client ID and Client Secret in `clarifai_tag.py` and `clarifai_search.py` to yours

2. Install requirements
  ```
  $ pip install requirements.txt
  ```

3. To tag images in images.txt, run:
  ```python
  python clarifai_tag.py
  ```

4. To search images from images.txt, tag the images first (i.e. run the above Python command) then run:
  ```
  python routes.py
  ```





