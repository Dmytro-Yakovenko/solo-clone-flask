import React from "react";
import Navigation from "../Navigation";
import "./AboutPage.css"
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry";
const images = [
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690382353/a6169d71aec018196a5590da4ad2b167_mzlqhc.jpg",
    alt: "food1",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690382348/23760acac7918992c874165274c4e7bb_i47aao.jpg",
    alt: "food2",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690382346/8cf8c26d79e7c94cf1c50a6260d06295_nqfld2.jpg",
    alt: "food3",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690382341/e987b4d781046ad57dd4ef25c2ac97dc_ltbt7l.jpg",
    alt: "food4",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690382340/505f07b3dab3ce5c01bb0838b84884f6_doa7sx.jpg",
    alt: "food5",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690382337/fe17801e424fdd4d53324a533aa505d7_a7ubbx.jpg",
    alt: "food6",
  },






  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690382333/01d9f84a2ac17fe69c5875d2624ecf4a_szarir.jpg",
    alt: "food7",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690382330/93e7b0fc55ba63d4bdc9a7154bf507ea_whcfyg.jpg",
    alt: "food8",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690067494/pexels-kamila-bairam-12123657_n8bwgu.jpg",
    alt: "food9",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690067382/pexels-valeria-boltneva-1639557_uhfhus.jpg",
    alt: "food10",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868810/pexels-vincent-rivaud-2295285_jrjr9q.jpg",
    alt: "food11",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868646/pexels-polina-tankilevitch-8601410_xln2nn.jpg",
    alt: "food12",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868414/pexels-max-ravier-10563267_mdgbsj.jpg",
    alt: "food13",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868220/pexels-maarten-van-den-heuvel-2284166_i6ptee.jpg",
    alt: "food14",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867882/pexels-chevanon-photography-323682_1_jkrutt.jpg",
    alt: "food15",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867051/pexels-senuscape-2313682_q11qva.jpg",
    alt: "food16",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866449/pexels-rajesh-tp-2098085_lylhr7.jpg",
    alt: "food17",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866146/pexels-prince-photos-3054690_bdu2rr.jpg",
    alt: "food18",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689865891/pexels-hana-brannigan-3642718_daru6k.jpg",
    alt: "food19",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689654276/pexels-robin-stickel-70497_1_ehdkcs.jpg",
    alt: "food20",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1673016571/samples/food/pot-mussels.jpg",
    alt: "food21",
  },



];
const AboutPage = () => {
  return (
    <>
      <Navigation />
      <div className="container about-page">

    <h1 className="about-page-title">Get your next dinner idea </h1>

        <ResponsiveMasonry columnsCountBreakPoints={{ 350: 2, 750: 4, 900: 7 }}>
          <Masonry columnsCount={7}>
            {images.map((item) => (
              <img className="images" key={item.alt} src={item.src} alt={item.alt} />
            ))}
          </Masonry>
        </ResponsiveMasonry>
      </div>
    </>
  );
};

export default AboutPage;
