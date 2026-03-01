  import pytest                                                                                                                                                                                                            
  from kalkulator import dodaj, odejmij, pomnoz, podziel                                                                                                                                                                   
                                                                                                                                                                                                                           
  def test_dodaj():                                                                                                                                                                                                        
      assert dodaj(2, 3) == 5                                                                                                                                                                                              
      assert dodaj(-1, 1) == 0

  def test_odejmij():
      assert odejmij(5, 3) == 2
      assert odejmij(0, 5) == -5

  def test_pomnoz():
      assert pomnoz(3, 4) == 12
      assert pomnoz(-2, 3) == -6

  def test_podziel():
      assert podziel(10, 2) == 5.0
      assert podziel(7, 2) == 3.5

  def test_podziel_przez_zero():
      with pytest.raises(ValueError):
          podziel(5, 0)
  EOF

