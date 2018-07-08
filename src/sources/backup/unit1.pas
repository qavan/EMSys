unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation
uses unit2,unit3,unit4;

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
  //Form1.Visible:=False;
  Form2.Show;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  //Form1.Visible:=False;
  Form3.Show;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  Form4.Show;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  Form5.Show;
end;



end.

