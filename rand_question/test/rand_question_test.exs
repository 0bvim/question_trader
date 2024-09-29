defmodule RandQuestionTest do
  use ExUnit.Case
  doctest RandQuestion

  test "greets the world" do
    assert RandQuestion.hello() == :world
  end
end
