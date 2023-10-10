import React from "react";
import "./AboutPage.css";
import { Redirect } from "react-router-dom";
import Masonry, { ResponsiveMasonry } from "react-responsive-masonry";
import { useSelector } from "react-redux";
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
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691268706/4990cfc15a4e2ee7028ecf016c1d511a_evc5ga.jpg",
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
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029732/617846d662268bf4b9a5707d2a4e4bd3_thdops.jpg",
    alt: "food22",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029732/0de94e3243c806d16bad26df0292ca84_wzhy61.jpg",
    alt: "food23",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029731/e391658e34b28ec036e67bab9bb20a21_n93q5x.jpg",
    alt: "food24",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029731/ced0454018c1dad6648100d6005c1a73_kfkqza.jpg",
    alt: "food25",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029731/86ca4b06d68315f197aeac77ad81c8c3_bouccd.jpg",
    alt: "food26",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029731/7c959584460b65f6726705aeb652381d_n1hqlw.jpg",
    alt: "food27",
  },

  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029731/5d8352714db363210ba538227583ca09_kobrni.jpg",
    alt: "food28",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690382330/93e7b0fc55ba63d4bdc9a7154bf507ea_whcfyg.jpg",
    alt: "food29",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029731/049a3681a774f4dd5683a2e51313e48e_zmxwrd.jpg",
    alt: "food30",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029731/f9094f5e4e60e7cb143ed0da72292948_afwwzm.jpg",
    alt: "food31",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029731/906505d3aca2f4bc46e2663721a04a69_rl7tte.jpg",
    alt: "food32",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029731/a38ce8ad1d9fd0198d6e723d7a15cd25_ke1una.jpg",
    alt: "food33",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029730/f597603d13ae0a46eef65bb923826183_znxerj.jpg",
    alt: "food34",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029730/6334ef773be514452d39b9f5d0e6c80c_mtyjk5.jpg",
    alt: "food35",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867882/pexels-chevanon-photography-323682_1_jkrutt.jpg",
    alt: "food36",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029730/e003f2493cf134abb2011a3ffd61058b_tunmg2.jpg",
    alt: "food37",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029730/5228bf78122e46144185c64e45cf5295_y6hzkr.jpg",
    alt: "food38",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029730/436e29b6115798c439fdb9bd320fbbeb_lg83vx.jpg",
    alt: "food39",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029730/b1f4f9fc4ab8cb1b6964387789af69c8_ldpmde.jpg",
    alt: "food40",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029730/07bd582832dfc519cc947aacefa40876_xnjch2.jpg",
    alt: "food41",
  },
  {
    src: "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691029729/dd89a500d22d60f7b993c454903cef3f_laippl.jpg",
    alt: "food42",
  },
];
const AboutPage = () => {
  const user = useSelector(state=>state.session.user)
  if(user){
    return <Redirect to="/pins"/>
  } 
<<<<<<< Updated upstream
  
=======
  console.log(user, 44444444)
>>>>>>> Stashed changes
  return (
    <>
      <div className="container about-page">
        <h1 className="about-page-title">Get your next dinner idea </h1>

        <ResponsiveMasonry columnsCountBreakPoints={{ 350: 2, 750: 4, 900: 7 }}>
          <Masonry columnsCount={7}>
            {images.map((item) => (
              <img
                className="images"
                key={item.alt}
                src={item.src}
                alt={item.alt}
              />
            ))}
          </Masonry>
        </ResponsiveMasonry>
      </div>
    </>
  );
};

export default AboutPage;
