unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Memo1: TMemo;
    Memo2: TMemo;
    Memo3: TMemo;
    Memo4: TMemo;
    Memo5: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  x:integer;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
  for x:=0 to Memo1.Lines.Count-1 do
  begin
    memo5.Lines.Add(Memo1.Lines.Strings[x]);memo5.Lines.Add(Memo3.Lines.Strings[x]);
    memo5.Lines.Add(Memo2.Lines.Strings[x]);memo5.Lines.Add(Memo4.Lines.Strings[x]);
    memo5.Lines.Add('#13');
  end;
end;

end.

