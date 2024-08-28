/* import { useEffect, useState } from "react";
import { BsArrowLeftCircleFill, BsArrowRightCircleFill } from "react-icons/bs";
import "./styles.css";

export default function ImageSlider({ url, limit = 5, page = 1 }) {
  const [images, setImages] = useState([]);
  const [currentSlide, setCurrentSlide] = useState(0);
  const [errorMsg, setErrorMsg] = useState(null);
  const [loading, setLoading] = useState(false);

  async function fetchImages(getUrl) {
    try {
      setLoading(true);

      const response = await fetch(`${getUrl}?page=${page}&limit=${limit}`);
      const data = await response.json();

      if (data) {
        setImages(data);
        setLoading(false);
      }
    } catch (e) {
      setErrorMsg(e.message);
      setLoading(false);
    }
  }

  function handlePrevious() {
    setCurrentSlide(currentSlide === 0 ? images.length - 1 : currentSlide - 1);
  }

  function handleNext() {
    setCurrentSlide(currentSlide === images.length - 1 ? 0 : currentSlide + 1);
  }

  useEffect(() => {
    if (url !== "") fetchImages(url);
  }, [url]);

  console.log(images);

  if (loading) {
    return <div>Loading data ! Please wait</div>;
  }

  if (errorMsg !== null) {
    return <div>Error occured ! {errorMsg}</div>;
  }

  return (
    <div className="container">
      <BsArrowLeftCircleFill
        onClick={handlePrevious}
        className="arrow arrow-left"
      />
      {images && images.length
        ? images.map((imageItem, index) => (
            <img
              key={imageItem.id}
              alt={imageItem.download_url}
              src={imageItem.download_url}
              className={
                currentSlide === index
                  ? "current-image"
                  : "current-image hide-current-image"
              }
            />
          ))
        : null}
      <BsArrowRightCircleFill
        onClick={handleNext}
        className="arrow arrow-right"
      />
      <span className="circle-indicators">
        {images && images.length
          ? images.map((_, index) => (
              <button
                key={index}
                className={
                  currentSlide === index
                    ? "current-indicator"
                    : "current-indicator inactive-indicator"
                }
                onClick={() => setCurrentSlide(index)}
              ></button>
            ))
          : null}
      </span>
    </div>
  );
} */

import { render, screen, fireEvent } from '@testing-library/react';
import ImageSlider from './ImageSlider';

describe('ImageSlider Component', () => {

  test('displays loading message while fetching images', () => {
    render(<ImageSlider url="test-url" />);
    expect(screen.getByText(/Loading data ! Please wait/i)).toBeInTheDocument();
  });

  test('displays error message if fetching images fails', async () => {
    global.fetch = jest.fn(() =>
      Promise.reject(new Error('Failed to fetch images'))
    );

    render(<ImageSlider url="test-url" />);
    const errorMsg = await screen.findByText(/Error occured !/i);
    expect(errorMsg).toBeInTheDocument();
  });

  test('displays images correctly after fetching', async () => {
    const mockImages = [
      { id: 1, download_url: 'image1.jpg' },
      { id: 2, download_url: 'image2.jpg' },
    ];

    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve(mockImages),
      })
    );

    render(<ImageSlider url="test-url" />);
    const img1 = await screen.findByAltText('image1.jpg');
    const img2 = await screen.findByAltText('image2.jpg');

    expect(img1).toBeInTheDocument();
    expect(img2).toBeInTheDocument();
  });

  test('navigates to the next image when the right arrow is clicked', async () => {
    const mockImages = [
      { id: 1, download_url: 'image1.jpg' },
      { id: 2, download_url: 'image2.jpg' },
    ];

    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve(mockImages),
      })
    );

    render(<ImageSlider url="test-url" />);
    const nextArrow = screen.getByRole('button', { name: /right/i });

    fireEvent.click(nextArrow);

    const img2 = await screen.findByAltText('image2.jpg');
    expect(img2).not.toHaveClass('hide-current-image');
  });

  test('loops back to the first image when the right arrow is clicked on the last image', async () => {
    const mockImages = [
      { id: 1, download_url: 'image1.jpg' },
      { id: 2, download_url: 'image2.jpg' },
    ];

    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve(mockImages),
      })
    );

    render(<ImageSlider url="test-url" />);
    const nextArrow = screen.getByRole('button', { name: /right/i });

    fireEvent.click(nextArrow); // First to second image
    fireEvent.click(nextArrow); // Should loop back to first image

    const img1 = await screen.findByAltText('image1.jpg');
    expect(img1).not.toHaveClass('hide-current-image');
  });

});