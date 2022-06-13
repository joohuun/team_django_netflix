const sliders = document.querySelector(".carouselbox")
var scrollPerClick;
var ImagePadding = 20
var scrollAmount = 0;

// 캐러셀 클래스 만들어보기
class Carousel {
    constructor(box) {
        this.sliders = document.querySelector(box);
        console.log(box);
        console.log(this.sliders)
    }

    sliderScrollLeft() {
        console.log("I'm left");
        this.sliders.scrollTo({
            top: 0,
            left: (scrollAmount -= 400),
            behavior: "smooth"
        });
        if (scrollAmount < 0) {
            scrollAmount = 0
        }
    }

    sliderScrollRight() {
        console.log("I'm right");
        if (scrollAmount <= this.sliders.scrollWidth - this.sliders.clientWidth) {
            this.sliders.scrollTo({
                top: 0,
                left: (scrollAmount += 400),
                behavior: "smooth",
            });
        }
    }
}

// 지금뜨는 컨텐츠
const recommend = new Carousel(".first");
// user가 찜한 컨텐츠
const userlike = new Carousel(".second");
// 평점 상위 컨텐츠
const ranking = new Carousel(".third");
// 상세페이지 관련영화 추천
const movie_related = new Carousel(".relation");