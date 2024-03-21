function Repas(props) {
  const { repas } = props;

  return (
    <>
    <div className="card" >
      <img src={repas.image} className="card--img-top" alt={repas.title} />
      <h5 className="card-title">{repas.title}</h5>
        <p className="card-text">{repas.description}</p>
        <button className="btn btn-primary">Go somewhere</button>
    </div>
      </>
    );
}

export default Repas;
